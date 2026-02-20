import ReactMarkdown from "react-markdown";
import { getIntegration } from "../../../lib/integrations";

export default async function Integration({ params }:{ params:{ slug:string } }){
  const { manifest, md } = await getIntegration(params.slug);
  return (
    <div>
      <div className="k">{manifest.category}</div>
      <div className="h1">{manifest.title}</div>
      <span className="badge">{manifest.status}</span>
      <hr style={{border:0,borderTop:"1px solid #1f2630",margin:"18px 0"}} />
      <ReactMarkdown>{md}</ReactMarkdown>
    </div>
  );
}
