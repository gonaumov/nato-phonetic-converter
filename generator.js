(() => {
const data = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".
split(",").map((item) => item.trim()).reduce((acc, curr) => { return `${acc}'${curr[0]}':'${curr}',\n` },'');
const element = document.createElement('a');
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
element.setAttribute('download', 'data.txt');
document.body.appendChild(element);
element.click();
})()