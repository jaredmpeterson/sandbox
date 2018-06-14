let args = process.argv.slice(2);
let sum = 0;

args.forEach(arg => {
  sum += Number(arg);
});

console.log(sum);
