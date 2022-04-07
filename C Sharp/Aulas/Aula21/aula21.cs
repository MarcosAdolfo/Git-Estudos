using System;

namespace Aula21
{

    class aula21
    {
        static void Main()
        {
            int num = 5;

            do//dowhile sempre vai roda uma vez, depois ele faz a verificassão 
            {
                Console.WriteLine(num);
            } while (num<5);

            string senha = "123";
            string senhaUser;

            do
            {
                Console.Clear();
                Console.Write("Senha: ");
                senhaUser = Console.ReadLine();
            } while (senhaUser != senha);
            Console.WriteLine("Senha Correta!!!");
        }
    }

}