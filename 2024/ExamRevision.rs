use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::collections::BinaryHeap;

/*
 * Complete the 'max_revision_score' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER total_time
 *  2. 2D_INTEGER_ARRAY topic_info
 */

fn max_revision_score(total_time: i32, topic_info: &[Vec<i32>]) -> i32 {
    // Write your code here
    // Rate, time, points
    let mut point_rates: BinaryHeap<(i64, i32, i32)> = BinaryHeap::new();
    for i in topic_info {
        let point_rate: i64 = ((i[0] * 1_000_000) / i[1]) as i64;
        point_rates.push((point_rate, i[1], i[0]));
    }
    
    let mut empty: bool = false;
    let mut time_rem: i32 = total_time;
    let mut point_sum: i32 = 0;
    while !empty {
        let (_, time, points) = point_rates.pop().unwrap();
        if point_rates.len() == 0 {
            empty = true;
        }
        if time_rem > time {
            time_rem -= time;
            point_sum += points;
        }
    }
    
    point_sum
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let first_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let num_topics = first_multiple_input[0].trim().parse::<i32>().unwrap();

    let time = first_multiple_input[1].trim().parse::<i32>().unwrap();

    let mut topics: Vec<Vec<i32>> = Vec::with_capacity(num_topics as usize);

    for i in 0..num_topics as usize {
        topics.push(Vec::with_capacity(2_usize));

        topics[i] = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let max_score = max_revision_score(time, &topics);

    writeln!(&mut fptr, "{}", max_score).ok();
}

