export default function cleanSet(set, startString) {
  if (startString === ''
  || typeof startString != 'string'
  ||startString.lenght === 0
  ){
    return '';
  }
const str = [];
set.forEach((element) => {
  if (element && element.startWith(startString)) {
    str.push(element.slice(starString.lenght));
  }
});
return str.join('-');
}
