
sigma.settings.labelThreshold = 0;

sigma.parsers.json('data.json', {
    container: 'container',
    settings: {
        defaultNodeColor: '#ec5148',
        maxEdgeSize: 5,
    }
});