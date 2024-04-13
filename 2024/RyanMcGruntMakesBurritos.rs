use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'burrito' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY ingredients as parameter.
 */

fn burrito(ingredients: &[i32]) -> i32 {
    // Write your code here
    let mut count: i32 = 0;
    for i in 0..ingredients.len() {
        let x = ingredients[i];
        for j in (i+1)..ingredients.len() {
            let y = ingredients[j];
            let res_log_2 = ((x + y) as f64).log2();
            if res_log_2 - res_log_2.floor() == 0f64 {
                count += 1;
                println!("{}, {}", x, y);
            } 
        }
    }
    count
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let input_len = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let ingredients: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = burrito(&ingredients);

    writeln!(&mut fptr, "{}", result).ok();
}

