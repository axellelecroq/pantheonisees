var traceH = {
    x: ["1791", "1794", "1806",
        "1807", "1808", "1809",
        "1810", "1811", "1812",
        "1813", "1814", "1815",
        "1829", "1885", "1889",
        "1894", "1907", "1908",
        "1920", "1925", "1933",
        "1948", "1949", "1952",
        "1964", "1987", "1988",
        "1989", "1995", "1996",
        "2002", "2011", "2015",
        "2018"
    ],
    y: [1, 1, 2,
        3, 6, 7,
        5, 6, 2,
        6, 3, 2,
        1, 1, 4,
        1, 2, 1,
        1, 1, 1,
        2, 3, 1,
        1, 1, 1,
        3, 1, 1,
        1, 1, 2,
        1,
    ],
    name: 'homme',
    type: 'bar',
    marker: {
        color: 'rgb(158,202,225)'
    },
    text: [
        "Voltaire",
        "Jean-Jacques Rousseau",
        "Claude Petiet, François Tronchet",
        "Jean-Baptiste Bévière, Jean-Etienne Portalis, Louis Resnier",
        "F. Béguinot, P. Cabanis, G. Caulaincourt, J. Malher, A. Praslin, J. Perregaux",
        "J. Vien, E. Crétet, G. Durazzo, J.-B. Papin, J. Sers, P. Garnier de la Boissière, J. Morard de Galle",
        "J.B. Treilhard, C. Claret de Fleurieu, J. Lannes, L. Leblond de Saint-Hilaire, G. Caprara",
        "L. Bougainville, M. Ordener, A. Sénarmont, J.-B. Songis de Courbons, C. Erskine, I. Vincent-Mareri",
        "Jean Doresenne-Le Paige, Jean Winter",
        "J. Jacqueminot, J. Rousseau, J. Viry, H. Cossé-Brissac, F. Walther, J. Lagrange",
        "Claude Régnier, Jean Démeunier, Jean Reynier",
        "Claude Legrand, Antoine Thévenard",
        "Jacques Soufflot",
        "Victor Hugo",
        "Jean Baudin, Théophile Corret de la Tour d'Auvergne, François Marceau, Lazare Carnot",
        "Sadi Carnot",
        "Marcellin Berthelot",
        "Emile Zola",
        "Léon Gambetta",
        "Jean Jaurès",
        "Paul Painlevé",
        "Paul Langevin, Jean Perrin",
        "Félix Éboué, Victor Schoelcher, Marc Schoelcher",
        "Louis Braille",
        "Jean Moulin",
        "René Cassin",
        "Jean Monnet",
        "Antoine Condorcet, Henri Grégoire, Gasparc Monge",
        "Pierre Curie",
        "André Malraux",
        "Alexandre Dumas",
        "Aimé Césaire",
        "Jean Zay, Pierre Brossolette",
        "Antoine Veil"
    ],
    hovertemplate: "<b>%{x}</b><br><br>" +
        "Nombre: %{y}<br>" +
        "Noms: %{text}<br>" +
        "<extra></extra>",

};

var traceF = {
    x: ["1791", "1794", "1806",
        "1807", "1808", "1809",
        "1810", "1811", "1812",
        "1813", "1814", "1815",
        "1829", "1885", "1889",
        "1894", "1907", "1908",
        "1920", "1925", "1933",
        "1948", "1949", "1952",
        "1964", "1987", "1988",
        "1989", "1995", "1996",
        "2002", "2011", "2015",
        "2018"
    ],
    y: [0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 1,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 1, 0,
        0, 0, 2,
        1,
    ],
    name: 'femme',
    type: 'bar',
    marker: {
        color: 'rgb(8,48,107)'
    },
    text: [
        "", "", "",
        "", "", "",
        "", "", "",
        "", "", "",
        "", "", "",
        "", "", "Sophie Berthelot",
        "", "", "",
        "", "", "",
        "", "", "",
        "", "Marie Curie", "",
        "", "", "Germaine Tillion, Geneviève de Gaulle-Anthonioz",
        "Simone Veil",


    ],
    hovertemplate: "<b>%{x}</b><br><br>" +
        "Nombre: %{y}<br>" +
        "Noms: %{text}<br>" +
        "<extra></extra>",

};

var data = [traceF, traceH];

var layout = {
    barmode: 'stack'
};

Plotly.newPlot('dataviz_pantheonisation', data, layout);