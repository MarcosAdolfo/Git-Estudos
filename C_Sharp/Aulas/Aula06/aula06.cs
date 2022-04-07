using System;

namespace Aula06
{

    class aula06
    {
        static void Main()
        {
            int n1,n2,n3;
            n1=10; n2=20; n3=15;
            Console.WriteLine(n1 + ", " + n2 + ", " + n3);
            Console.Write("\n\tn1 = {0} \n\tn2 = {1} \n\tn3 = {2}\n",n1,n2,n3); //\n quebra de linha; \t tabulação

            double valoDeCompra = 2.75;
            double valoDeVenda;
            double lucro = 0.1;
            string produto = "Pastel";

            valoDeVenda = valoDeCompra+(valoDeCompra*lucro);

            Console.WriteLine("Produto......:{0,15}",produto);
            Console.WriteLine("Val.compra...:{0,15:c}",valoDeCompra);
            Console.WriteLine("Lucro........:{0,15:p}",lucro);
            Console.WriteLine("Val.venda....:{0,15:c}",valoDeVenda);
        }
    }

}