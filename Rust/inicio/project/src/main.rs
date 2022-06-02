use std :: io;
mod matt;

fn main()
{
    let nome = "M.A";
    //nome = "Marcos Adolfo" ERRO! não mutável

    let mut txt: String = "Texto".to_string();
    txt = "Texto De Teste".to_string();

    let mut txt1: String = String::from("New Texto");
    txt1 = "Novo Texto De Teste".to_string();

    let mut imput: String = String::new();

    println!("Hello, world!");
    println!("Olá, Mundo!");
    println!("Nome: {}", nome);
    println!("{}\n{}", txt,txt1);

    println!("Inicia [S/N]:");
    io::stdin().read_line(&mut imput)
        .ok()
        .expect("Error!!!");
    println!("Escolha: {}",imput);

    matt::Quadrado();
}
