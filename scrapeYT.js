var links = document.querySelectorAll('a#video-title.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer')
data = {}
links.forEach((link, index) =>{
    var title = link.textContent.trim()
    var vid = link.getAttribute('href').split('&')[0].split('=')[1]
    data[title] = {'index': index+1, 'vid': vid }
})
console.log(data)