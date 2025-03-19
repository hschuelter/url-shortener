import { useState } from "react";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Card, CardContent } from "./ui/card";
import { Label } from "./ui/label"
import { Copy, Loader2 } from "lucide-react";
import { toast } from "sonner";

const API_URL = import.meta.env.VITE_API_URL

function URLShortener() {
	const [url, setUrl] = useState("");
	const [shortUrl, setShortUrl] = useState(null);
	const [loading, setLoading] = useState(false);


	function isValidHttpUrl(string: string) {
		try {
			const newUrl = new URL(string);
			return newUrl.protocol === 'http:' || newUrl.protocol === 'https:';
		} catch (err) {
			return false;
		}
	}

	const handleInputChange = (e) => {
		let inputValue = e.target.value;

		if (url == '' && (!inputValue.startsWith("http://") || !inputValue.startsWith("https://"))) {
			inputValue = 'https://' + inputValue;
		}

		setUrl(inputValue);
	};

	const handleShorten = async () => {
		if (!isValidHttpUrl(url)) {
			console.log('Erro: url', url);
			return toast.error("Please enter a valid URL");
		}
		setLoading(true);

		try {
			var request = {
			'url': url
			}
			const response = await fetch(API_URL + '/shorten', {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(request)
			});
			const data = await response.json();
			// console.log(data);
			// console.log(data.short_url);
			setShortUrl(data.short_url)
		} catch (error) {
			toast.error("Something went wrong");
		}
		setLoading(false);
	};

	const handleCopy = () => {
		if (shortUrl) {
			navigator.clipboard.writeText(API_URL + '/' + shortUrl);
			toast.success("Copied to clipboard!");
		}
	};

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Card className="w-full max-w-3xl p-4 bg-white shadow-xl rounded-2xl">
		
		<div className="flex flex-col pl-6">
			<Label className="text-3xl  font-bold  self-start space-y-4 "> Shorten your link </Label>
			<Label className="text-base font-light self-start pb-16"> For free! </Label>
		</div>

        <CardContent className="flex flex-col space-y-4">
			<Input
				className="p-4 h-12"
				placeholder="https://example.com/my-url"
				value={url}
				type="url"
				onChange={handleInputChange}
			/>

			<div className="flex">
				<Button className="max-w-40 p-4 text-lg h-12" onClick={handleShorten} disabled={loading}>
					{loading ? <Loader2 className="animate-spin text-xl" /> : "Get your link"}
				</Button>
				{shortUrl && (
					<div className="flex items-center justify-between p-2 ml-6 border rounded-lg h-12 min-w-40">
						<span className="truncate max-w-[80%]">{shortUrl}</span>
						<Button size="icon" variant="default" onClick={handleCopy}>
							<Copy className="w-5 h-5" />
						</Button>
					</div>
				)}

			</div>
        </CardContent>
      </Card>
    </div>
  );
}

export default URLShortener;