import type { NextPage } from "next";
import Head from "next/head";
import Navbar from '@/components/Navbar'

const Home: NextPage = () => {
    return (
        <>
            <Head>
                <title>Joshua's Portfolio</title>
                <meta name="description" content="Generated by create-t3-app" />
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="w-screen min-h-screen bg-slate-900 flex justify-center items-center">
                <div className="w-full flex flex-col justify-center overflow-y-scroll items-center space-y-6">
                    <Title />
                    <Description />
                    <Nav />
                </div>
            </main>
        </>
    );
};

const Title: React.FC = _ => (
    <h2 className="text-[3rem] lg:text-[5rem] md:text-[5rem] font-extrabold text-white">
        Hi, I'm <span className="text-blue-700">Joshua Ji</span>
    </h2>
)

const Description: React.FC = _ => (
    <div className="flex flex-col justify-center items-center space-y-2">
        <p className="text-2xl text-slate-400">I'm a computer science student studying at the University of Alberta.</p>
        <p className="text-2xl text-slate-400">I love working with the web and stuff.</p>
    </div>
)

const Nav: React.FC = _ => (
    <span className='text-lg p-4' >
        <Navbar atHome />
    </span>
)

export default Home;
