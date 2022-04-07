// See https://aka.ms/new-console-template for more information
// <ImplicitUsings>disable</ImplicitUsings>
using System;


namespace BALTA
{

    class Program
    {
        static void Main(string[] args)
        {
            int num = 100;
            float real = 25.5f;

            num = (int)real;
            num = Convert.ToInt32(real);
            
            MeuMetodo();

            Produto mouse = new Produto();
            var teclado = new Produto(003, "Teclado Gamer", 226.78,EProdutoType.Produto);

            Console.WriteLine(mouse.Id);
            Console.WriteLine(teclado.Id);
            Console.WriteLine(teclado.Type);
        }

        static void MeuMetodo()
        {
            Console.WriteLine("C# é legal!");
        }
    }

    struct Produto
    {
        public Produto(int id, string name, double price, EProdutoType type)
        {
            Id = id;
            Nome = name;
            Price = price;
            Type = type;
        }
        public int Id;
        public string Nome;
        public double Price;
        public EProdutoType Type;

        public double PriceInDolar(double dolar)
        {
            return Price * dolar;
        }
    }

    enum EProdutoType
    {
        Produto = 1,
        Service = 2
    }
}
