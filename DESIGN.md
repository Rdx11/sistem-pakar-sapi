# DESIGN.md — Frontend UI Conventions

## Visual Identity
- **Primary color**: `yellow-500` (`#eab308`) — buttons, badges, active borders, progress bars
- **Backgrounds**: `gray-50` page, white cards, `yellow-50` / `yellow-100` highlights
- **Accent**: `yellow-600` (`#ca8a04`) for icons and hover states
- **Font**: Inter via system font stack (`Inter, system-ui, -apple-system, sans-serif`)
- **Shadows**: custom yellow-tinted (`shadow-yellow-sm` through `shadow-yellow-xl`, defined in `tailwind.config.js`)

## Component Patterns
- **Cards**: `bg-white rounded-2xl shadow-sm border border-gray-100 p-8`
- **Buttons**: `bg-yellow-500 hover:bg-yellow-600 text-white font-bold px-8 py-3.5 rounded-xl transition shadow-lg shadow-yellow-200`
- **Inputs**: `w-full border border-gray-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition`
- **Badges**: `<span class="font-mono text-xs font-semibold text-yellow-600 bg-yellow-100 px-2 py-0.5 rounded">{{ g.kode }}</span>`
- **Progress bars**: `bg-gradient-to-r from-yellow-400 to-yellow-500 h-3 rounded-full`
- **Icons**: All inline SVG inside `<svg>` elements (no icon library)

## Stack
- Tailwind CSS 3.4 (standalone CLI, not a PostCSS plugin)
- Alpine.js 3.14 (`defer` in `<head>`, `x-data`, `x-model`, `x-show`, `x-transition`, `@click`)
- Custom CSS in `static/css/custom.css` — scrollbar, transitions, button press, pulse animation

## Build
```sh
npm run build   # compiles static/css/input.css → static/css/main.css
```
Tailwind scans `./templates/**/*.html` for class usage. Run `build` (or `watch`) before serving after template changes.

## Layout
- Navbar: white with bottom border, SVG logo + "SiPakar Sapi", auth-conditional menu links
- Main: `flex-1 max-w-5xl mx-auto px-4 py-8 w-full`
- Footer: centered, gray, "Sistem Pakar Penyakit Sapi — Metode Certainty Factor — Kabupaten Sumbawa — © 2025"
- Django messages rendered as dismissable Alpine alerts at top of `<main>`

## Interactivity (Alpine.js)
- **Diagnosa form**: `x-data="{ dipilih: [], cari: '' }"` — checkbox tracking, live search filter, disable submit when 0 selected
- **Riwayat table**: `x-data="{ cari: '' }"` — filter rows by nama_pemilik or penyakit
- **Hasil accordion**: `x-data="{ buka: true/false }"` — expand/collapse per disease detail
- **Messages**: `x-data="{ show: true }"` — dismissable flash messages

## Conventions
- All templates extend `base.html`
- Page title blocks: `{% block title %}...{% endblock %}`
- Use `{% static '...' %}` for CSS and JS assets
- Form inputs use `POST` with `{% csrf_token %}`
- Responsive grid: `grid grid-cols-1 md:grid-cols-2` or `md:grid-cols-3`
- Every section heading has an inline SVG icon to the left
- Buttons have `flex items-center gap-2` pattern with inline SVGs
