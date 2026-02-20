import './globals.css';
import Link from 'next/link';
export const metadata={title:'OpenTalons'};
export default function RootLayout({children}:{children:React.ReactNode}){return (<html lang='en'><body><div className='nav'><b>OpenTalons</b><Link href='/'>Home</Link><Link href='/skills'>Skills</Link><Link href='/integrations'>Integrations</Link></div><div className='container'>{children}</div></body></html>)}
