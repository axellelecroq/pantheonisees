var trace2 = {
    x: ['Architecte du panthéon', 'Artiste', 'Explorateur', "Personnes de lettres", "Personnes de loi", "Militaire", "Parent.e", "Politique ", "Religieux.se", "Résistant.e", "Révolution", "Scientifique"],
    y: [1, 1, 1, 6, 3, 18, 1, 27, 4, 2, 1, 10],
    name: 'Homme',
    type: 'bar',
    marker: {
        color: 'rgb(158,202,225)'
    },
    text: [
        'Jacques-Germain Soufflot',
        'Joseph Vien',
        'Louis-Antoine Bougainville',
        'Alexandre Dumas, Emile Zola, Victor Hugo, Jean-Jacques Rousseau, Voltaire, Aimé Césaire',
        'Jean-Ignace Jacqueminot, Claude-Ambroise Regnier, Jean-Baptiste Treilhard',
        "François Marceau, Téophile Corret de la Tour d'Auvergne, Claude Legrand, ...",
        "March Schoelcher",
        "André Malraux, Jean Monnet, Sadie Carno, Jean Rouseau, Jean-Pierre Sers, Jean Zay, ...",
        "Henri Grégoire, Ippolito Vincent-Mareri, Charles Erskine, Giovanni Caprara",
        "Jean Moulin, René Cassin",
        "Jean Perregaux",
        "Pierre Cabanis, Pierre Curie, Gaspard Monge, Louis Braille, Marcellin Berthelot, ..."
    ],
    hovertemplate: "<b>%{x}</b><br><br>" +
        "Nombre: %{y}<br>" +
        "Noms: %{text}<br>" +
        "<extra></extra>",

};

var trace1 = {
    x: ['Architecte du panthéon', 'Artiste', 'Explorateur', "Personnes de lettres", "Personnes de loi", "Militaire", "Parent.e", "Politique ", "Religieux.se", "Résistant.e", "Révolution", "Scientifique"],
    y: [0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 2],
    name: 'Femme',
    type: 'bar',
    marker: {
        color: 'rgb(8,48,107)'
    },
    text: [
        "", "", "", "", "", "", "Sophie Berthelot", "Simone Veil", "", "Geneviève de Gaulle-Anthonioz, Germaine Tillion", "", "Marie Curie"
    ],
    hovertemplate: "<b>%{x}</b><br><br>" +
        "Nombre: %{y}<br>" +
        "Noms: %{text}<br>" +
        "<extra></extra>",
};


var data = [trace1, trace2];

var layout = {
    barmode: 'stack'
};

Plotly.newPlot('dataviz_status', data, layout);