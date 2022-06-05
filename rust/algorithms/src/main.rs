fn main() {
    println!("{:?}", egyptian_fractions3(5, 121));
}
fn egyptian_fractions(a: u128, b: u128) -> Vec<u128> {
    let mut v = Vec::new();
    if a == 1 {
        v.push(b);
        println!("{}", b);
        return v;
    }

    let mut a = a;
    let mut b = b;
    'outer: loop {
        if a == 1 {
            v.push(b);
            break 'outer;
        }
        let t = (b - b % a) / a + 1;
        v.push(t);
        println!("t= {},a= {},b= {}", t, a, b);
        a = a * t - b;
        b = b * t;

    }
    return v;
}

fn egyptian_fractions3(a: u128, b: u128) -> Vec<u128> {
    let mut v = Vec::new();
    let mut a = a;
    let mut b = b;
    loop {
        println!("a= {},b= {}", a, b);
        if a == 1 {
            v.push(b);
            break;
        }
        let t = (b - b % a) / a + 1;
        println!("{}", t);
        v.push(t);
        a = a * t - b;
        b = b * t;
    }
    v
}
