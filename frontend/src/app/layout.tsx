import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Master Analytics Platform | Full-Stack Architect',
  description: 'Enterprise Data Solutions & Social Impact Dashboard',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
