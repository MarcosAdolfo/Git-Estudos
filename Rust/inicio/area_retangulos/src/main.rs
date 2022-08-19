#[derive(Debug)]
struct Retangulo
{
    altura: u32,
    largura: u32,
}
fn main()
{
    let rec1 = Retangulo{altura:50, largura:80};

    println!("O {:?} tem a Area de:",rec1);
    println!("Area: {}", area(&rec1));
}

fn area(retangulo: &Retangulo) -> u32
{
    retangulo.altura * retangulo.largura
}
