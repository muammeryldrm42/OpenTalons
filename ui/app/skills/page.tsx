import Link from "next/link";
import { getPacks, getPackIndex } from "../../lib/skills";

export default async function Skills({ searchParams }:{ searchParams:{ pack?: string } }){
  const packs = await getPacks();
  const pack = searchParams.pack ?? packs[0];
  const idx = await getPackIndex(pack);
  return (
    <div>
      <div className="h1">Skills</div>
      <div>{packs.map(p=> <Link key={p} className="badge" href={`/skills?pack=${encodeURIComponent(p)}`}>{p}</Link>)}</div>
      <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
      <div className="cardgrid">
        {idx.skills.map((s:any)=>(
          <Link key={s.slug} className="card" href={`/skills/${encodeURIComponent(pack)}/${encodeURIComponent(s.slug)}`}>
            <div className="k">{s.category}</div>
            <div style={{fontSize:18,fontWeight:700}}>{s.name}</div>
            <div>{(s.permissions?.length? s.permissions : ["no permissions"]).map((p:string)=> <span key={p} className="badge">{p}</span>)}</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
