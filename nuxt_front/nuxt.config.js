export default {
    components: true,
    head: {
        titleTemplate: 'Chone Koja | %s',
        htmlAttrs: {
            lang: 'fa',
            dir: 'rtl'
        },
        bodyAttrs: {
            class: 'container'
        },
        meta: [
            { charset: 'utf-8' },
            { hid: 'viewport', name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: 'Find the places to stay overnight during your trip.' },
            { hid: "og:title", name: "keywords", content: "Home, Rent, Searc, Trip, cheap, good", },
            {
                hid: "og:author",
                name: "author",
                content: "Amir Hossein Roohi",
            },
        ],
        // link: [
        //     { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        // ],
        link: [
            { rel: 'stylesheet', type: 'text/css', href: 'https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma-rtl.min.css' }
        ]
    }
}