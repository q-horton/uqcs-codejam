use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::collections::BinaryHeap;

/*
 * Complete the 'order_execution' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER num_tasks
 *  2. INTEGER num_priorities
 *  3. INTEGER_ARRAY tasks
 *  4. INTEGER_ARRAY priorities
 */

fn order_execution(num_tasks: i32, num_priorities: i32, tasks: &[i32], priorities: &[i32]) -> Vec<i32> {
    // Write your code here
    let mut values: BinaryHeap<(i32, i32, i32)> = BinaryHeap::new();
    for i in 0..(num_tasks as usize) {
        values.push((num_priorities - priorities[i], i as i32, tasks[i]));
    }
    
    let mut output: Vec<i32> = Vec::new();
    while values.len() > 0 {
        let (_, _, task) = values.pop().unwrap();
        output.push(task);
    }
    output
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let num_tasks = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let num_priorities = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let tasks: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let priorities: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let order = order_execution(num_tasks, num_priorities, &tasks, &priorities);

    for i in 0..order.len() {
        write!(&mut fptr, "{}", order[i]).ok();

        if i != order.len() - 1 {
            write!(&mut fptr, " ").ok();
        }
    }

    writeln!(&mut fptr).ok();
}

