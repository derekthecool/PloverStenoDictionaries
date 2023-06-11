open System
Seq.initInfinite(fun _->Console.ReadLine())
|>Seq.takeWhile(fun x->x<>null)
|>Seq.skip 0
|>Seq.iter(printfn "%A")
