use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'quaternions' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts 2D_INTEGER_ARRAY q as parameter.
 */

fn quat_prod(q1: &Vec<i64>, q2_raw: &Vec<i32>) -> Vec<i64> {
    let mut q2: Vec<i64> = Vec::new();
    for i in q2_raw {
        q2.push(*i as i64);
    }
    
    let a: i64 = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3];
    let b: i64 = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2];
    let c: i64 = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1];
    let d: i64 = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0];
    Vec::from([a, b, c, d])
}

fn quaternions(q: &[Vec<i32>]) -> Vec<i64> {
    // Write your code here
    let mut result: Vec<i64> = Vec::from([1, 0, 0, 0]);
    
    for i in q {
        result = quat_prod(&result, i);
    }
    
    result
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let nn = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let mut qq: Vec<Vec<i32>> = Vec::with_capacity(nn as usize);

    for i in 0..nn as usize {
        qq.push(Vec::with_capacity(4_usize));

        qq[i] = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let yy = quaternions(&qq);

    for i in 0..yy.len() {
        write!(&mut fptr, "{}", yy[i]).ok();

        if i != yy.len() - 1 {
            write!(&mut fptr, " ").ok();
        }
    }

    writeln!(&mut fptr).ok();
}

