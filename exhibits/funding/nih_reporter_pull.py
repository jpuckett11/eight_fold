import json,urllib.request,time,sys
URL="https://api.reporter.nih.gov/v2/projects/search"
def page(text,off,fy=(2024,2025)):
    body={"criteria":{"fiscal_years":list(fy),
          "advanced_text_search":{"operator":"and","search_field":"projecttitle,abstracttext,terms","search_text":text}},
          "include_fields":["ProjectNum","FiscalYear","AwardAmount","Organization","ProjectTitle","AgencyIcAdmin"],
          "offset":off,"limit":500}
    r=urllib.request.Request(URL,data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r,timeout=120))
def total(text):
    got=[];off=0
    while True:
        d=page(text,off); tot=d["meta"]["total"]; res=d.get("results",[])
        got+=res; off+=len(res)
        if off>=tot or not res or off>=8000: break
        time.sleep(0.4)
    return tot,got
TERMS=[t.strip() for t in open(sys.argv[1]) if t.strip()]
out={}
for t in TERMS:
    n,rows=total(t)
    dollars=sum(r.get("award_amount") or 0 for r in rows)
    ics={}
    for r in rows:
        ic=(r.get("agency_ic_admin") or {}).get("abbreviation","?")
        ics[ic]=ics.get(ic,0)+(r.get("award_amount") or 0)
    top=sorted(ics.items(),key=lambda x:-x[1])[:3]
    out[t]={"projects":n,"dollars":dollars,"top_ic":top,"rows":rows}
    print(f"{t:<44} {n:>6} projects  ${dollars/1e6:>10,.1f}M   " + ", ".join(f"{k} ${v/1e6:.0f}M" for k,v in top),flush=True)
json.dump({k:{kk:vv for kk,vv in v.items() if kk!="rows"} for k,v in out.items()},open("summary.json","w"),indent=1)
json.dump({k:v["rows"] for k,v in out.items()},open("rows.json","w"))
