import fs from 'fs';
import type { NextRequest } from "next/server";

export const POST = async (req: NextRequest) => {
    const body = await req.json();
    const json = fs.readFileSync("data/preferences.json", "utf-8");

    let data = []
    if (json != "") { data = JSON.parse(json); }
    data.push(body)

    fs.writeFileSync('data/preferences.json', JSON.stringify(data));
    return new Response("Submitted")
}