import xml.etree.ElementTree as ET
import fitz
import re

def comparar_nf_com_pedido(xml_file, pdf_file):
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    tree = ET.parse(xml_file)
    root = tree.getroot()

    nf_items = []
    for det in root.findall('.//nfe:det', ns):
        prod = det.find('nfe:prod', ns)
        imposto = det.find('nfe:imposto', ns)
        icms = imposto.find('.//nfe:ICMS51', ns)
        ipi = imposto.find('.//nfe:IPITrib', ns) or imposto.find('.//nfe:IPINT', ns)

        nf_items.append({
            "codigo": prod.findtext('nfe:cProd', default='', namespaces=ns),
            "descricao": prod.findtext('nfe:xProd', default='', namespaces=ns),
            "ncm": prod.findtext('nfe:NCM', default='', namespaces=ns),
            "icms": float(icms.findtext('nfe:pICMS', default='0', namespaces=ns)) if icms is not None else None,
            "ipi": float(ipi.findtext('nfe:pIPI', default='0', namespaces=ns)) if ipi is not None else 0.0
        })

    doc = fitz.open(pdf_file)
    pedido_text = "\n".join(page.get_text() for page in doc)

    pedido_items = []
    pattern = re.compile(r"Referência:\s*(\S+).*?NCM:\s*(\d+).*?ICMS\s+(\d{1,2}\.\d{2})%.*?IPI\s+(\d{1,2}\.\d{2})%", re.DOTALL)
    for match in pattern.finditer(pedido_text):
        codigo, ncm, icms, ipi = match.groups()
        pedido_items.append({
            "codigo": codigo.strip(),
            "ncm": ncm.strip(),
            "icms": float(icms),
            "ipi": float(ipi)
        })

    relatorio = []
    for nf in nf_items:
        match = next((p for p in pedido_items if p["codigo"] == nf["codigo"]), None)
        if match:
            relatorio.append({
                "produto": nf["descricao"],
                "codigo": nf["codigo"],
                "verificacoes": {
                    "ncm": {"nf": nf["ncm"], "pedido": match["ncm"], "ok": nf["ncm"] == match["ncm"]},
                    "icms": {"nf": nf["icms"], "pedido": match["icms"], "ok": nf["icms"] == match["icms"]},
                    "ipi": {"nf": nf["ipi"], "pedido": match["ipi"], "ok": nf["ipi"] == match["ipi"]}
                }
            })
        else:
            relatorio.append({
                "produto": nf["descricao"],
                "codigo": nf["codigo"],
                "verificacoes": "Item não encontrado no pedido"
            })

    return relatorio
