use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main()
{
    println!("Adivinhe o Numero!");

    let secret_num = rand::thread_rng().gen_range(1..101);

    //println!("O numero secreto é: {}", secret_num);

    loop
    {

        println!("Por favor digite seu numero");

        let mut resp = String::new();

        io::stdin()
            .read_line(&mut resp)
            .expect("Failed to read");

        let resp: u32 = match resp.trim().parse()
        {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Você escolheu: {}", resp);

        match resp.cmp(&secret_num)
        {
            Ordering::Less => println!("Muito pequeno!"),
            Ordering::Greater => println!("Muito grande!"),
            Ordering::Equal => {
                println!("Você Ganhou!");
                break;
            }
        }
    }
}
