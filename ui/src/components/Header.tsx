import { Label } from "./ui/label"

function Header() {
	return (
		<>
			<div className="flex flex-col bg-black">
				<Label className="text-white font-mono text-2xl m-4 ml-6 self-start"> 
					<a className="text-white hover:text-white" href="https://encurta-ai.vercel.app/">
						encurta.ai 
					</a>
				</Label>
			</div>
		</>
	);
}
export default Header;
