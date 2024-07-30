                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[+] All messages sent. Restarting the process...\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
