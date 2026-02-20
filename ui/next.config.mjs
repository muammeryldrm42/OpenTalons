import path from "node:path";

/** @type {import('next').NextConfig} */
const nextConfig = {
  outputFileTracingRoot: path.join(process.cwd(), ".."),
  typescript: { ignoreBuildErrors: true },
  eslint: { ignoreDuringBuilds: true },
};

export default nextConfig;