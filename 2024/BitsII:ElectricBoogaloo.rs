use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'bits_2_electric_boogaloo' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts LONG_INTEGER_ARRAY a as parameter.
 */

fn bits_2_electric_boogaloo(a: &[i64]) -> Vec<i64> {
    // Write your code here
    let mut output: Vec<i64> = Vec::new();
    for i in a {
        let mut shift: i32 = 0;
        loop {
            if i & (1 << shift) == 0 {
                output.push(i + (1 << shift));
                break;
            }
            shift += 1;
        }
    }
    output
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let nn = stdin_iterator.next().unwrap().unwrap().trim().parse::<i64>().unwrap();

    let mut aa: Vec<i64> = Vec::with_capacity(nn as usize);

    for _ in 0..nn {
        let aa_item = stdin_iterator.next().unwrap().unwrap().trim().parse::<i64>().unwrap();
        aa.push(aa_item);
    }

    let yy = bits_2_electric_boogaloo(&aa);

    for i in 0..yy.len() {
        write!(&mut fptr, "{}", yy[i]).ok();

        if i != yy.len() - 1 {
            writeln!(&mut fptr).ok();
        }
    }

    writeln!(&mut fptr).ok();
}

