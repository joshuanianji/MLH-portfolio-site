import Link from 'next/link';
import { useRouter } from 'next/router';
import { OrderedMap } from 'immutable';

const pages = OrderedMap({
    'home': '/',
    'about': '/about',
    'projects': '/projects',
    'experience': '/experience'
})

const NavbarElem: React.FC<{ label: string, link: string, atEnd: boolean }> = props => {
    const router = useRouter();

    return (
        <>
            <span className={`${router.pathname === props.link ? 'text-blue-500' : 'text-white'} hover:text-blue-500`}>
                <Link href={props.link}>{`'${props.label}'`}</Link>
            </span>
            {props.atEnd ? '' : ','}
        </>
    )
}

interface NavbarProps {
    atHome: boolean;
};

const Navbar: React.FC<NavbarProps> = ({ atHome }) => {
    // if we're at the home page, do not show the "home" link
    const newPages = atHome ? pages.delete('home') : pages;

    // make the navbar look like a list
    return (
        <div className='flex flex-row space-x-3 font-mono text-white'>
            <span>[</span>
            {Array.from(newPages).map(([label, link], n) => <NavbarElem label={label} link={link} key={n} atEnd={n === newPages.size - 1} />)}
            <span>]</span>
        </div>
    )
}

export default Navbar;