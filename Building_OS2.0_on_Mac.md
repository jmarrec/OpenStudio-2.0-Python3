
# Building OpenStudio 2.X on Mac


## Version:
Tested with the following:

    MacOS Sierra 10.12.2	
    ccmake version 3.7.0
    Xcode 8.1, Build version 8B62 (no reason it shouldn't work with XCode 8.2)
    
## Procedure

1.Clone the git repository and checkout the develop branch. `cd`to the location where you want to put the OpenStudio folder

    git clone https://github.com/NREL/OpenStudio.git

2.Enter the newly created `OpenStudio` folder

    cd OpenStudio

3.Checkout the develop branch

    git checkout develop

4.I suggest keeping the folder in which you'll build outside of the OpenStudio/ folder, that'll be easier to completely delete all files
    cd ..
    mkdir OS-build && cd OS-build/

5.Call ccmake to build the `OpenStudio/openstudiocore` source directory and NOT the root source

    ccmake ../OpenStudio/openstudiocore

6.Configure (press `[c]`)

This will download a lot of dependencies, and will finally likely throw out an error about missing OpenSSL: on Mac OS X 10.11 and above the development headers are no longer included.

If you get the openssl error: `brew install openssl`

In CCMake, Enable the detailed configuration by pressing `[t]`.

Find and configure the OPENSSL options:

* `OPENSSL_INCLUDE_DIR = /usr/local/opt/openssl/include`
* `OPENSSL_CRYPTO_LIBRARY = /usr/local/opt/openssl/lib/libcrypto.a`
* `OPENSSL_SSL_LIBRARY = /usr/local/opt/openssl/lib/libssl.a`

It's possible your openssl version might be in your Cellar if it's not in /usr/local/opt
(try `brew link --force openssl`, and `brew list openssl`)

Configure again (press `[c]`), this time it should work.

Then generate and quit (press `[g]`)

7.Type `make`

If it breaks with the following error (I no longer get that problem):

    make[2]: *** No rule to make target `src/utilities/idd/IddFieldEnums.ixx', needed by `openstudio_utilities_static_HeadersGenerated_done.stamp'.  Stop.
    make[1]: *** [src/utilities/CMakeFiles/openstudio_utilities_static_GeneratedHeaders.dir/all] Error 2

Type the following two commands (still in the `./build` directory):

    make GenerateIddFatory
    make GenerateIddFactoryRun

Now retype `make`. This time it should work!

