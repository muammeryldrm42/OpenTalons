import ReactMarkdown from "react-markdown";
import { getSkill } from "../../../../lib/skills";

export default async function SkillDetail({ params }:{ params:{ pack:string; slug:string } }){
  const { md, manifest } = await getSkill(params.pack, params.slug);
  return (
    <div>
      <div className="k">{params.pack}</div>
      <div className="h1">{manifest.name}</div>
      <div>{(manifest.permissions?.length? manifest.permissions : ["no permissions"]).map((p:string)=> <span key={p} className="badge">{p}</span>)}</div>
      <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
      <ReactMarkdown>{md}</ReactMarkdown>
      <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
      <pre style={{whiteSpace:"pre-wrap"}}>{JSON.stringify(manifest,null,2)}</pre>
    </div>
  );
}
