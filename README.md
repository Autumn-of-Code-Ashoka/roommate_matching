# roommate_matching
A project to automate optimal matchings between roommates based on their preferences

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

To get started on the web-app,

First, change directory to webapp:

```bash
cd ./webapp
```

Then, install all dependencies:

```bash
npm i
# or
yarn i
# or
pnpm i
# or
bun i
```

Then, rename `preferences.json.example` to `preferences.json`.

Finally, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Matching Algorithm

To build on the matching algorithm,

First, change directory to matching_algorithm:

```bash
cd ./matching_algorithm
```

Run `algorithm.py` to generate the roommmate matches.

Open `mail.py` to process these matches from `matches.json` and email the results.

[Irving's Matching Algorithm](https://en.wikipedia.org/wiki/Stable_roommates_problem) - learn more about the implementation

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
