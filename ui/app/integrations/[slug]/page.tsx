import Link from "next/link";

type Params = { slug: string };

export default async function IntegrationPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;

  return (
    <main className="mx-auto w-full max-w-4xl px-6 py-10">
      <div className="mb-6">
        <Link href="/integrations" className="text-sm underline opacity-80 hover:opacity-100">
          ← Back to integrations
        </Link>
      </div>

      <h1 className="text-3xl font-semibold">Integration</h1>
      <p className="mt-2 opacity-80">
        Slug: <span className="font-mono">{slug}</span>
      </p>
    </main>
  );
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  return {
    title: `${slug} • Integrations`,
    description: `Integration details for ${slug}`,
  };
}