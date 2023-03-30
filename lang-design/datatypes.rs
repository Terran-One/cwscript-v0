contract DataTypesTest {
    instantiate() {
      // primitives
      none
      string
      bool
      byte = u8
  
      // rust
      u / i {8,16,32,64,128}
    
      // builtin
      int
      dec<6> // decimal with precision of 6
    
      // composites
      [1, 1, 1] // -- list (aka vector), all of same type
      (1, "hi") // -- tuple
  
      Item() // tuple type    
  
      // struct type
      Config {
        owner: "123123",
        count: 0
      }
  
      // object type
      {
        a: 24,
        b: 3
      }
  
      // monads
      ok ( ... )
      err ( ... )
  
    }
  }
  
  contract ResultsTest {
  
    instantiate() {
      // checked sub
      let a = 5
      let b = 6
  
      let a = Uint128::from(5);
      let b = Uint128::from(6);
  
      try {
        
      } catch {
        
      }
      let c = a.checked_sub(b);
    
      let a = 5
      let b
    }
  
  }