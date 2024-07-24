export const metadata = {
	title: "Next.js",
	description: "Generated by Next.js",
	hello: 'hello from Root layout',
	world: 'this world is mine'
};

export default function RootLayout({ children }) {
	return (
		<html lang="en">
			<body>
				<header
					style={{
						backgroundColor: "lightblue",
						padding: "1rem",
					}}
				>
					<h1>header</h1>
				</header>
				{children}
				<footer
					style={{
						backgroundColor: "lightcoral",
						padding: "1rem",
					}}
				>
					<h1>footer</h1>
				</footer>
			</body>
		</html>
	);
}
