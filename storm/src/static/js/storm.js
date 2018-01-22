/* event listener */
document.getElementsByName("ordem")[0].addEventListener('change', ordenaFilmes);

/* checking for the current variables */
function regexReplaceUrlSearch(url, key, value){
	var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
	var separator = url.indexOf('?') !== -1 ? "&" : "?";
	if (url.match(re)) {
		return url.replace(re, '$1' + key + "=" + value + '$2');
	} else {
		return url + separator + key + "=" + value;
	}
}

/* redirects us for the correct url on change */
function ordenaFilmes() {
	var url = window.location.href;
	var key = 'ordem';
	var value = this.value;
	window.location.href = regexReplaceUrlSearch(url, key, value);
}