using System;

namespace Aula44
{

    struct Carro
    {
        public string marca;
        public string modelo;
        public string cor;

        public Carro(string marca, string modelo, string cor)
        {
            this.marca = marca;
            this.modelo = modelo;
            this.cor = cor;
        }
    }

    class aula44
    {
        static void Main()
        {
            Carro c1;
            Carro c2 = new Carro("Honda","HRV","Preto");

            c1.marca = "VW";
            c1.modelo = "Golf";
            c1.cor = "Branco";

            Console.WriteLine("Marca c1/c2.: {0} / {1}", c1.marca, c2.marca);
            Console.WriteLine("Modelo c1/c2: {0} / {1}", c1.modelo,c2.modelo);
            Console.WriteLine("Cor c1/c2...: {0} / {1}", c1.cor,c2.cor);
        }       
    }

}