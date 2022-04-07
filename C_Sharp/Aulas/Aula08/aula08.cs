using System; 

namespace Aula08
{

    class aula08Settings
    {
        static void Main()
        {
            int v1,v2,soma;
            string nome;

            Console.Write("Digite seu Nome: ");
            nome = Console.ReadLine();
            Console.WriteLine("Nome: "+nome);

            Console.Write("Digite o primeiro Numero: ");
            v1 = int.Parse(Console.ReadLine());
            Console.Write("Digite o Segundo Numero: ");
            v2 = Convert.ToInt32(Console.ReadLine());
            soma = v1 + v2;
            Console.WriteLine("A soma de {0} mais {1} é igual a {2}",v1,v2,soma);
        }
    }

}
