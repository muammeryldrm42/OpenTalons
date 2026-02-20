import Link from "next/link";
import { getIntegrations } from "../../lib/integrations";

export default async function Integrations(){
  const items = await getIntegrations();
  const grouped = items.reduce((acc:any, it:any)=>{ (acc[it.category] ||= []).push(it); return acc; }, {});
  return (
    <div>
      <div className="h1">Integrations</div>
      {Object.entries(grouped).map(([cat, list]:any)=>(
        <div key={cat}>
          <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
          <div style={{fontSize:18,fontWeight:700}}>{cat}</div>
          <div className="cardgrid" style={{marginTop:12}}>
            {list.map((it:any)=>(
              <Link key={it.name} className="card" href={`/integrations/${encodeURIComponent(it.name)}`}>
                <div className="k">{it.status}</div>
                <div style={{fontSize:18,fontWeight:700}}>{it.title}</div>
                <div style={{color:"#9fb1c1",marginTop:6}}>{it.description}</div>
              </Link>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
