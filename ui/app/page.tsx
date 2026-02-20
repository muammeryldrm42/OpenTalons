import Link from "next/link";
import { getPacks } from "../lib/skills";
import { getIntegrations } from "../lib/integrations";

export default async function Home(){
  const packs = await getPacks();
  const integrations = await getIntegrations();
  return (
    <div>
      <div className="k">secure-by-default</div>
      <div className="h1">OpenTalons</div>
      <p>Catalog UI (no run yet). Vercel-ready.</p>
      <div>
        <span className="badge">{packs.length} packs</span>
        <span className="badge">200 skills</span>
        <span className="badge">{integrations.length} integrations</span>
      </div>
      <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
      <div className="cardgrid">
        <Link className="card" href="/skills"><div className="k">browse</div><div style={{fontSize:18,fontWeight:700}}>Skills</div></Link>
        <Link className="card" href="/integrations"><div className="k">browse</div><div style={{fontSize:18,fontWeight:700}}>Integrations</div></Link>
      </div>
    </div>
  );
}
