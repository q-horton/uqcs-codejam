use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'maximum_money' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY list_money as parameter.
 */

fn maximum_money(list_money: &[i32]) -> i32 {
    // Write your code here
    let min_cost: i32 = *list_money.iter().min().unwrap();
    let max_cost: i32 = *list_money.iter().max().unwrap();
    
    let mut curr_score: i32 = 0;
    for i in min_cost..=max_cost {
        let mut count: i32 = 0;
        for j in list_money {
            if *j >= i {
                count += 1;
            }
        }
        if count * i > curr_score {
            curr_score = count * i;
        }
    }
    curr_score
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let number_of_students = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let mut moneys: Vec<i32> = Vec::with_capacity(number_of_students as usize);

    for _ in 0..number_of_students {
        let moneys_item = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();
        moneys.push(moneys_item);
    }

    let index = maximum_money(&moneys);

    writeln!(&mut fptr, "{}", index).ok();
}

