// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://docs.kdesp73.org',
	integrations: [
		starlight({
			title: 'My Docs',
			description: 'Documentation, notes and tutorials for various topics.',
			logo: {
				src: './src/assets/identicon.png',
			},
			editLink: {
				baseUrl: 'https://github.com/KDesp73/Docs/edit/main/',
			},
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/KDesp73' },
				{ icon: 'linkedin', label: 'LinkedIn', href: 'https://www.linkedin.com/in/konstantinos-despoinidis' },
			],
			customCss: ['./src/styles/custom.css'],
			sidebar: [
				{ label: 'About', slug: 'about' },
				{
					label: 'Notes',
					items: [{ autogenerate: { directory: 'posts/notes', collapsed: true } }],
				},
				{
					label: 'Documentation',
					items: [{ autogenerate: { directory: 'posts/documentation', collapsed: true } }],
				},
				{
					label: 'Tutorials',
					items: [{ autogenerate: { directory: 'posts/tutorials', collapsed: true } }],
				},
				{
					label: 'Papers',
					items: [{ autogenerate: { directory: 'posts/papers', collapsed: true } }],
				},
				{
					label: 'Misc',
					items: [{ autogenerate: { directory: 'posts/misc', collapsed: true } }],
				},
			],
			lastUpdated: true,
		}),
	],
});
