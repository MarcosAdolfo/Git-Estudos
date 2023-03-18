fn main()
{
    let mut num = 10;
    ts_point(&mut num);
    println!("Hello, world!: {}", num);
}

fn ts_point(pont:&mut i32)
{
    *pont = *pont * 2;
}
