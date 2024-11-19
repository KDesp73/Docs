---
title: Publish a Maven Package
date: 2024-11-19 18:51:00 +0200
categories: [tutorial] 
tags: [java, maven]
---

## Step 0: Create a Sonatype account

Visit [central.sonatype.com](https://central.sonatype.com/) and follow the appropriate steps to create an account and get a verified namespace

> Signing up using Github is recommended to simplify the process

## Step 1: Get your User Token

Navigate to your [account](https://central.sonatype.com/account) and click `Generate User Token`

![token-image](./assets/token/step.png)

## Step 2: Set-up settings-security.xml

Run the following command

```bash
$ mvn --encrypt-master-password
```

Enter a master password and the output should look something like the following

`{hashed-password}`

Create the `~/.m2/settings-security.xml` file and write the following xml

```xml
<settingsSecurity>
    <master>hashed-password</master>
</settingsSecurity>

```

## Step 3: Create a gpg key for signing

If not already installed, install gnupg in your system

### Generate GPG Key

```bash
$ gpg --full-generate-key
```

You will be prompted to provide the following information:

1. Key Type: Choose RSA and RSA (default).
2. Key Size: Enter 4096 for a secure key.
3. Key Expiration: Choose a duration (e.g., 0 for no expiration, or 1y for one year).
4. Name: Enter your name (this will be publicly visible).
5. Email Address: Enter the email address associated with your Sonatype account.
6. Comment: Leave this blank or add an optional note.

After confirming the details, set a secure passphrase for your private key.

### List your keys

```bash
gpg --list-keys
```

Look for the key ID under the pub section, which will look something like this:

```css
pub   rsa4096 2024-11-19 [SC]
      ABCD1234EF567890GHIJK1234567890ABCDEF123
uid           [ultimate] Your Name <your.email@example.com>
sub   rsa4096 2024-11-19 [E]
```

The long string (e.g., ABCD1234EF567890GHIJK1234567890ABCDEF123) is your key fingerprint.


### Publish your public key

```bash
gpg --send-keys --keyserver hkps://keys.openpgp.org <key-id>
```

## Step 4: Set-up settings.xml

Create the `~/.m2/settings.xml` file and add the following xml

```xml
<settings>
    <servers>
        <server>
            <id>central</id> <!-- Name this however you like -->
            <username>sonatype_token_username</username>
            <password>sonatype_token_password</password>
        </server>
    </servers>

    <profiles>
        <profile>
            <id>gpg</id>
            <properties>
                <gpg.executable>gpg</gpg.executable>
                <gpg.passphrase>your-secure-passphrase</gpg.passphrase>
            </properties>
        </profile>
    </profiles>
    <activeProfiles>
        <activeProfile>gpg</activeProfile>
    </activeProfiles>
</settings>

```

`your-secure-passphrase` can be encrypted using `mvn`

```bash
mvn --encrypt-password "your-secure-passphrase"
```

Use the hashed output instead of `your-secure-passphrase`

## Step 5: Configure your pom.xml

### Add the necessary information

The following are taken from my [DataBridge](https://github.com/KDesp73/DataBridge) library

```xml
<groupId>io.github.kdesp73</groupId>
<artifactId>DataBridge</artifactId>
<version>2.0.14</version>
<packaging>jar</packaging>

<name>DataBridge</name>
<description>A Java library for managing database connections and transactions</description>
<url>https://github.com/KDesp73/DataBridge</url>

<licenses>
  <license>
    <name>MIT</name>
    <url>https://rem.mit-license.org/license.txt</url>
    <distribution>repo</distribution>
  </license>
</licenses>

<developers>
  <developer>
    <id>KDesp73</id>
    <name>Konstantinos Despoinidis</name>
    <email>despoinidisk@gmail.com</email>
  </developer>
</developers>

<scm>
  <url>https://github.com/KDesp73/DataBridge</url>
  <connection>scm:git:git://github.com/KDesp73/DataBridge.git</connection>
  <developerConnection>scm:git:ssh://git@github.com:KDesp73/DataBridge.git</developerConnection>
  <tag>HEAD</tag>
</scm>
```

### Distribution Management

```xml
<distributionManagement>
  <snapshotRepository>
    <id>central</id> <!-- same as settings.xml -->
    <url>https://s01.oss.sonatype.org/content/repositories/snapshots</url>
  </snapshotRepository>
  <repository>
    <id>central</id> <!-- same as settings.xml -->
    <url>https://s01.oss.sonatype.org/service/local/staging/deploy/maven2/</url>
  </repository>
</distributionManagement>
```

### Plugins

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-gpg-plugin</artifactId>
  <version>3.1.0</version>
  <executions>
    <execution>
      <id>sign-artifacts</id>
      <phase>verify</phase>
      <goals>
        <goal>sign</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

```xml
<plugin>
  <groupId>org.sonatype.central</groupId>
  <artifactId>central-publishing-maven-plugin</artifactId>
  <version>0.6.0</version>
  <extensions>true</extensions>
  <configuration>
    <publishingServerId>central</publishingServerId> <!-- same as settings.xml -->
    <autoPublish>true</autoPublish>
    <waitUntil>uploaded</waitUntil>
  </configuration>
</plugin>
```
```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-source-plugin</artifactId>
  <version>2.2.1</version>
  <executions>
    <execution>
      <id>attach-sources</id>
      <goals>
        <goal>jar-no-fork</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-javadoc-plugin</artifactId>
  <version>2.9.1</version>
  <executions>
    <execution>
      <id>attach-javadocs</id>
      <goals>
        <goal>jar</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

## Step 6: Deploy your package

```bash
$ mvn clean verify

$ mvn clean deploy
```
