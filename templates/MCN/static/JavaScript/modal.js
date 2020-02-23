$('#Modal').on('hidden.bs.modal', function () {
    callPlayer('yt-player', 'stopVideo');
});