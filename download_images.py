import requests
import os

# List of image URLs 
image_urls = [
    "https://64.media.tumblr.com/efa53b8a041f78815b14886e19c97d64/e0eaf099b3e3da5f-eb/s500x750/67b1b308534558ffd2eb7ac721a045decc838449.jpg",
    "https://64.media.tumblr.com/1067dd0379634759d4d239d837d1eaf0/e0eaf099b3e3da5f-31/s500x750/e3f06cce0d9bd01c568ee731c6af8e2bf5f18aea.jpg",
    "https://64.media.tumblr.com/2d60bf1c44989c0e650076cec9538c66/e0eaf099b3e3da5f-34/s500x750/b6ddc9ec8353583d6b8b27dc0eb4f5ad58757bf2.jpg",
    "https://64.media.tumblr.com/fbef051fdb9a286099b60ce203683b78/e0eaf099b3e3da5f-16/s500x750/e475350cd670ad0f52b21fd587f25d5c0980a62f.jpg",
    "https://64.media.tumblr.com/7bd594f4105c9a616cff6434c4810116/e0eaf099b3e3da5f-02/s500x750/a7afe9dfe51e5c99b0ca7217d5cce1e424002b45.jpg",
    "https://64.media.tumblr.com/cd90e3c54889d045b5299b1f831323ee/e0eaf099b3e3da5f-b7/s500x750/64d3017bc102a3c3bd7e74710268e56129164ff5.jpg",
    "https://64.media.tumblr.com/a6b1a645a1b0f08011148ebbabdbcc9a/e0eaf099b3e3da5f-78/s500x750/e4df2ddef1a3fef7c21209c08164bbbb6006d294.jpg", 
    "https://64.media.tumblr.com/f2936fb5d536437a17e61922b756e021/e0eaf099b3e3da5f-b0/s500x750/00fa64dd6d3eab264c2d845c87d71050dc364700.jpg",
    "https://64.media.tumblr.com/8d01fb62110ec4a2036550f448442c6f/e0eaf099b3e3da5f-cf/s500x750/21c792d0d8e9b02a76c76abc5a522b45bd2b44a5.jpg", 
    "https://64.media.tumblr.com/5fdc1a1fd7d47c93e5566cd2bc6f5f27/e0eaf099b3e3da5f-59/s500x750/1b96b4c3c9000989f549ed2b1c9ed0bea81dfa28.jpg",
    "https://64.media.tumblr.com/180f9218269cc7b1b7c492c9048849c6/e0eaf099b3e3da5f-d5/s500x750/c9fd7f0837b64d9816a10d13a239ca5eb3ae52d5.jpg",
    "https://assets.tumblr.com/images/default_avatar/cone_closed_16.png",
    "https://64.media.tumblr.com/be12991362017b2ec8138ede981e048c/93ca21d59ad15b27-30/s16x16u_c1/9f5c6dc889d35dff8b20b2e0f0b7a2d909ef1236.pnj",
    "https://assets.tumblr.com/images/default_avatar/cone_open_16.png",
    "https://64.media.tumblr.com/9f94984f78a2f1b3a4d0ad5026c62c9d/86afa327d2542148-5a/s16x16u_c1/9a461512fe773b8e49fa841337b67bd5d7e9e303.pnj",
    "https://64.media.tumblr.com/adbd84cb4d39713cc3e3e7bec90bd009/ec3d2217b4d49e4f-a0/s16x16u_c1/6a31e080cc4c95c599285f2d0afcc20d5fd3eda1.pnj",
    "https://assets.tumblr.com/images/default_avatar/cube_blue_green_16.png",
    "https://64.media.tumblr.com/24e4655c10f73f996e22f3c98e441e8d/265ca28cfb87ba0c-ac/s16x16u_c1/a7b3cde2c73e3ad621c8fb4494be72f971c2303f.pnj",
    "https://64.media.tumblr.com/0090a820dbb5dbd7106987926c5f2b76/e34a508a6eaa2453-57/s16x16u_c1/269fcc6a1c5e2ba6686b3ebf4f56e0416c2d33b1.jpg",
    "https://64.media.tumblr.com/d3209de53cd07380d361bd4ccdd4f26f/099846c36fb54506-04/s16x16u_c1/98054e2d9d4e6a675e1bf68cd31acefcf1e8b72d.pnj",
    "https://64.media.tumblr.com/c847309794ebea0261deb4d19048ef46/b7a482a09d23bac7-c2/s16x16u_c1/660ffc9730820693eeaef96cbace14f4cbc29657.pnj",
    "https://assets.tumblr.com/images/default_avatar/pyramid_purple_blue_16.png",
    "https://assets.tumblr.com/images/default_avatar/pyramid_purple_blue_16.png",
    "https://64.media.tumblr.com/1be70ce9b5a6da30a74236ac33a9d2be/ca89ec34e5c0b3c5-37/s16x16u_c1/ecce27b12d3fac5883ece1fa91f3f60eef132a83.jpg",
    "https://64.media.tumblr.com/0b5b63695c10098ceb9b3219b8850701/faa7a52581aede00-fe/s16x16u_c1/4fedf8a967e22c0cbd9b7e04a62c0c6ba6d008b8.pnj",
    "https://64.media.tumblr.com/c47824fc809de0c72f95c84b212615cb/ac80543415302c61-5d/s16x16u_c1/a3d5ae41ed3da089d1b9038e00dc3a47dfe8ca48.pnj",
    "https://64.media.tumblr.com/52bf5a3821a6973622b183ca5d9fa515/8bbd037148fe1324-f0/s16x16u_c1/88091f620a173cca3c552d61699475262526a469.pnj",
    "https://assets.tumblr.com/images/default_avatar/sphere_open_16.png",
    "https://64.media.tumblr.com/154289d77bb43370fc63d04e1f67597b/040413f631028968-6e/s16x16u_c1/7cac3d40e1114568e39f76021066a1724387b38b.jpg",
    "https://64.media.tumblr.com/281bc245f648b0b5ae1a57897d4dd246/cd72a9ab534a2ea7-5e/s16x16u_c1/d2aae998a18bff063e79606b147ffe42371b5af1.pnj",
    "https://64.media.tumblr.com/6668653d31fc4b57cd1702aa5b1cff2f/00ef61ff23f3ded8-2b/s16x16u_c1/54b59281488f313ca0d09b8ad065db5dc37c4a3b.pnj",
    "https://64.media.tumblr.com/a49cbb5848bf804e4d6240c38d328d04/a2028ade1ebc95b9-7b/s16x16u_c1/b0ff48f2facfc7262d25386df7ee29b5bdf826ec.pnj",
    "https://64.media.tumblr.com/db03a6cabfbbd2b4a3ca428cad196187/7c025c1d66208eaf-53/s16x16u_c1/9a65fe720484680cecb7e2a05027b5b39a37d1a5.pnj",
    "https://64.media.tumblr.com/0def47992fb2f46fb65d143a67c23f22/a78bd259c0887943-e2/s16x16u_c1/0a4d4eda0c933a08abde33553de74d1cee78a2f3.jpg",
    "https://64.media.tumblr.com/517548748dc1575e28731d55c9deaa10/87a0c496d103ed3f-f5/s16x16u_c1/c30aeb2575348fc36cfd8f4d0b70a9cc9dd75701.jpg",
    "https://64.media.tumblr.com/7be33e1ad89b1da53e48c1d5d480acf1/8cd05e38a098ac25-49/s16x16u_c1/c67f36a1d8f1506b8ce42c90848eda265c5ac838.pnj",
    "https://64.media.tumblr.com/bd3747d5e520a8d22b7c8345cb494f74/05127f692a42f88f-0f/s16x16u_c1/30a020e6cd01cbb02fd5877e9790a9cfce6a53e2.jpg",
    "https://64.media.tumblr.com/f49be5784a60940d4d06a8f3c5b9481f/3410baca67c216cb-88/s16x16u_c1/21ba2cdda68aeec771786d1d029047c3da00e661.jpg",
    "https://64.media.tumblr.com/c3c2fd4a4bd988213a443ac3fae086da/e6fd8cddb5d7d45d-62/s16x16u_c1/d8dfbcef007a7926c1a06c85d4a8023816ad38a3.pnj",
    "https://64.media.tumblr.com/ecff476dc00011197007bbdaaefb9572/7feb88bc663436f6-fe/s16x16u_c1/525935b25928a69fea60e20c7736b09c846fd8ca.pnj",
    "https://64.media.tumblr.com/191b4668a2a70904bf9eda614dd0b011/d6719049d401009f-60/s16x16u_c1/2e801930c4553b06e52bc06ed38af06454245543.pnj",
    "https://64.media.tumblr.com/avatar_2293dc67fa14_16.pnj",        
    "https://64.media.tumblr.com/24f9328aa8b537995bdef748074cad9b/754ce6b1e189cf48-0d/s16x16u_c1/76d701da51574c19f8ba72417ba1df33ade853b4.jpg",
    "https://64.media.tumblr.com/9657cec5e27bb0eb87284e0469d6c9a2/7df72265f6620dad-1a/s16x16u_c1/d02933f392346427af753790a96b4a30e8afa532.jpg",
    "https://64.media.tumblr.com/0fa0891bcb9cf7243229933d0a8a30ae/dd48a2992d4d4ed8-b8/s16x16u_c1/dc4d563e306f018cbe842aa5c57d84fe5ad27f62.pnj",
    "https://64.media.tumblr.com/f23061ad96a6cc5e059c9ec775bf9537/e4a5cec6f47cf85d-c4/s16x16u_c1/baac04bc50f8d14d6b5f6218dae03fc1244a1671.pnj",
    "https://assets.tumblr.com/images/default_avatar/pyramid_closed_16.png",
    "https://64.media.tumblr.com/fae849cad42bcd0d70ed73da93f8ad3a/bc85738111f6251f-37/s16x16u_c1/fef6e745e340798bc521081a16d2e773bc7bfe32.pnj",
    "https://64.media.tumblr.com/e1fc6b055d5d790d9bb649f0982a2e0d/bc6d2e2e3e30966d-12/s16x16u_c1/58a3df0328783533c9353c24c7f54883cbd191f8.pnj",
    "https://64.media.tumblr.com/2d289034b54924b319fc7abbec2230aa/996f96c5d9638afb-c9/s16x16u_c1/dda755cc6d1aa43bf9acaa305a8b9874b34678ca.jpg",
    "https://64.media.tumblr.com/657533d978421f9cb4d9ea7e947bf6ea/58eaf369df1e9a83-ca/s16x16u_c1/80a9905ec59c1fcaa31eb496bc258ba11e556a91.pnj",
    "https://64.media.tumblr.com/0b2a6dd55838b7807b424a5b6927706b/edf11724d9b2e595-ff/s16x16u_c1/f06a3a5713124957c2243d92e06ae3cb182e30e5.jpg",
    "https://64.media.tumblr.com/231072748e137f342f74a2de43effde9/29951345031a600c-22/s16x16u_c1/b19ed98a30409f254c1a38c984c2311b06072704.pnj",
    "https://64.media.tumblr.com/e511bad376b9ee62deda5ee1083d0407/9fa982b44190e264-66/s16x16u_c1/696b58c6634ce314245fdf148e49b5cf1c6b1a41.m/impixu?T=1740303848&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly8xN3RoLWFuZ2VsLnR1bWJsci5jb20vcG9zdC80MDEyNTEzODI1Ny9zaGluamktaWthcmktcmFpc2luZy1wcm9qZWN0LWdhbWUtd2l0aC10aGUtc2NlbmVzIiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJwb3N0cyI6W3sicG9zdGlkIjoiNDAxMjUxMzgyNTciLCJibG9naWQiOjMwMjQ5NDY1LCJzb3VyY2UiOjMzfV0sIm5vc2NyaXB0IjoxfQ==&U=AAPGMEKHJO&K=747425ac8c539be6d7211ae17ff031e7856a7a773e0ca8c0bb72dc61995ebdc9&R=",
]

# Create a folder to save images
folder_name = "downloaded_images"
os.makedirs(folder_name, exist_ok=True)

# Download each image
for idx, img_url in enumerate(image_urls, start=1):
    response = requests.get(img_url)
    if response.status_code == 200:
        image_path = os.path.join(folder_name, f"image_{idx}.jpg")
        with open(image_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {image_path}")
    else:
        print(f"Failed to download {img_url}")

print("All images downloaded!")